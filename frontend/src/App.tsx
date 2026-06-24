import { useEffect, useState } from "react";
import axios from "axios";

import AttackGraph
from "./components/AttackGraph";

type DashboardData = {
  scans: number;
  findings: number;
  sql_injection: number;
  xss: number;
};

type Finding = {
  id: number;
  title: string;
  severity: string;
  tool: string;
  file_path: string;
  line_number: number;
};

type FindingDetail = {
  id: number;
  title: string;
  severity: string;
  description: string;
  tool: string;
  file_path: string;
  line_number: number;

  ai_exploitability: string;
  ai_confidence: number;
  ai_remediation: string;
  ai_attack_narrative: string;
};

type Correlation = {
  category: string;
  severity: string;
  count: number;
  findings: number[];
};

type AttackPath = {
  title: string;
  likelihood: string;
  impact: string;
  priority: string;
  risk_score: number;

  attack_chain: string[];

  mitre: {
    id: string;
    name: string;
  }[];
};

function normalizeTitle(
  title: string
) {
  const lower =
    title.toLowerCase();

  if (
    lower.includes("sql") ||
    lower.includes("tainted-sql")
  ) {
    return "SQL Injection";
  }

  if (
    lower.includes("xss") ||
    lower.includes("format-string")
  ) {
    return "Cross Site Scripting";
  }

  if (
    lower.includes("github")
  ) {
    return "GitHub Token";
  }

  if (
    lower === "aws" ||
    lower.includes("aws-access-token")
  ) {
    return "AWS Secret";
  }

  if (
    lower.includes("api key") ||
    lower.includes("generic-api-key")
  ) {
    return "API Key";
  }

  if (
    lower.includes("secret")
  ) {
    return "Hardcoded Secret";
  }

  return title;
}

function severityColor(
  severity: string
) {
  if (
    severity === "ERROR"
  ) {
    return "#ef4444";
  }

  if (
    severity === "WARNING"
  ) {
    return "#f59e0b";
  }

  return "#22c55e";
}

function App() {
  const [dashboard, setDashboard] =
    useState<DashboardData | null>(
      null
    );

  const [findings, setFindings] =
    useState<Finding[]>([]);

  const [selectedFinding, setSelectedFinding] =
    useState<FindingDetail | null>(
      null
    );

  const [correlations, setCorrelations] =
    useState<Correlation[]>([]);

  const [attackPaths, setAttackPaths] =
    useState<AttackPath[]>([]);

  useEffect(() => {

    axios
      .get(
        "http://localhost:8000/dashboard"
      )
      .then((response) => {
        setDashboard(
          response.data
        );
      });

    axios
      .get(
        "http://localhost:8000/findings/latest"
      )
      .then((response) => {
        setFindings(
          response.data
        );
      });

    axios
      .get(
        "http://localhost:8000/correlation"
      )
      .then((response) => {
        setCorrelations(
          response.data
        );
      });

    axios
      .get(
        "http://localhost:8000/ai-attack-paths"
      )
      .then((response) => {
        setAttackPaths(
          response.data.attack_paths
        );
      });

  }, []);

  const loadFinding = async (
    id: number
  ) => {

    try {

      const response =
        await axios.get(
          `http://localhost:8000/finding/${id}`
        );

      setSelectedFinding(
        response.data
      );

    } catch (error) {

      console.error(
        error
      );

    }
  };

  if (!dashboard) {

    return (
      <div className="container">
        <h2>
          Loading Dashboard...
        </h2>
      </div>
    );

  }

  return (

    <div className="container">

      <h1>
        AttackGraph AI
      </h1>

      <h2>
        Security Dashboard
      </h2>

      <div className="metric-grid">

        <div className="metric-card">
          <h3>
            Total Scans
          </h3>

          <p>
            {dashboard.scans}
          </p>
        </div>

        <div className="metric-card">
          <h3>
            Total Findings
          </h3>

          <p>
            {dashboard.findings}
          </p>
        </div>

        <div className="metric-card">
          <h3>
            SQL Injection
          </h3>

          <p>
            {dashboard.sql_injection}
          </p>
        </div>

        <div className="metric-card">
          <h3>
            XSS
          </h3>

          <p>
            {dashboard.xss}
          </p>
        </div>

      </div>

      <h2>
        Findings
      </h2>

      <table>

        <thead>

          <tr>
            <th>Title</th>
            <th>Severity</th>
            <th>Tool</th>
            <th>File</th>
            <th>Line</th>
          </tr>

        </thead>

        <tbody>

          {findings.map(
            (finding) => (

              <tr
                key={finding.id}
                onClick={() =>
                  loadFinding(
                    finding.id
                  )
                }
              >

                <td>
                  {
                    normalizeTitle(
                      finding.title
                    )
                  }
                </td>

                <td>

                  <span
                    style={{
                      background:
                        severityColor(
                          finding.severity
                        ),
                      color:
                        "white",
                      padding:
                        "5px 10px",
                      borderRadius:
                        "6px",
                      fontWeight:
                        "bold",
                      fontSize:
                        "12px"
                    }}
                  >
                    {
                      finding.severity
                    }
                  </span>

                </td>

                <td>
                  {
                    finding.tool
                  }
                </td>

                <td>
                  {
                    finding.file_path
                  }
                </td>

                <td>
                  {
                    finding.line_number
                  }
                </td>

              </tr>

            )
          )}

        </tbody>

      </table>

      {!selectedFinding && (

        <div
          style={{
            marginTop: "20px",
            textAlign: "center"
          }}
        >
          <p>
            Select a finding
            to view AI analysis
          </p>
        </div>

      )}

      {selectedFinding && (

        <div className="details-panel">

          <h2>
            {
              normalizeTitle(
                selectedFinding.title
              )
            }
          </h2>

          <p>
            <strong>
              Severity:
            </strong>
            {" "}
            {
              selectedFinding.severity
            }
          </p>

          <p>
            <strong>
              Exploitability:
            </strong>
            {" "}
            {
              selectedFinding.ai_exploitability
            }
          </p>

          <p>
            <strong>
              Confidence:
            </strong>
            {" "}
            {
              Math.round(
                selectedFinding.ai_confidence * 100
              )
            }
            %
          </p>

          <h3>
            Remediation
          </h3>

          <pre>
            {
              selectedFinding.ai_remediation
            }
          </pre>

          <h3>
            Attack Narrative
          </h3>

          <pre>
            {
              selectedFinding.ai_attack_narrative
            }
          </pre>

        </div>

      )}

      <h2
        style={{
          marginTop: "50px"
        }}
      >
        Correlated Findings
      </h2>

      <div
        className="correlation-grid"
      >

        {correlations.map(
          (item, index) => (

            <div
              key={index}
              className="correlation-card"
            >

              <h3>
                {item.category}
              </h3>

              <p>
                <strong>
                  Severity:
                </strong>
                {" "}
                {item.severity}
              </p>

              <p>
                <strong>
                  Findings:
                </strong>
                {" "}
                {item.count}
              </p>

            </div>

          )
        )}

      </div>

      {attackPaths.length > 0 && (

        <div className="top-risk-card">

          <h2>
            Highest Risk Attack Path
          </h2>

          <h3>
            {
              attackPaths[0].title
            }
          </h3>

          <p>
            Risk Score:
            {" "}
            {
              attackPaths[0]
                .risk_score
            }
          </p>

          <p>
            Priority:
            {" "}
            {
              attackPaths[0]
                .priority
            }
          </p>

        </div>

      )}

      <h2>
        Attack Graph Visualization
      </h2>

      <AttackGraph />


      <h2
        style={{
          marginTop: "50px"
        }}
      >
        AI Attack Paths
      </h2>

      <div className="attack-path-grid">

        {attackPaths.map(
          (path, index) => (

            <div
              key={index}
              className="attack-card"
            >

              <h3>
                {path.title}
              </h3>

              <p>
                <strong>
                  Risk Score:
                </strong>
                {" "}
                {path.risk_score}
              </p>

              <p>
                <strong>
                  Priority:
                </strong>
                {" "}
                {path.priority}
              </p>

              <p>
                <strong>
                  Likelihood:
                </strong>
                {" "}
                {path.likelihood}
              </p>

              <p>
                <strong>
                  Impact:
                </strong>
                {" "}
                {path.impact}
              </p>

              <h4>
                Attack Chain
              </h4>

              <ul>

                {path.attack_chain.map(
                  (
                    step,
                    i
                  ) => (

                    <li key={i}>
                      {step}
                    </li>

                  )
                )}

              </ul>

              <h4>
                MITRE ATT&CK
              </h4>

              <ul>

                {path.mitre.map(
                  (
                    technique,
                    i
                  ) => (

                    <li key={i}>
                      {
                        technique.id
                      }
                      {" - "}
                      {
                        technique.name
                      }
                    </li>

                  )
                )}

              </ul>

            </div>

          )
        )}

      </div>

    </div>

  );
}

export default App;