import ReactFlow from "reactflow";
import "reactflow/dist/style.css";

export default function AttackGraph() {

  const nodes = [
    {
      id: "1",
      position: { x: 100, y: 100 },
      data: { label: "SQL Injection" }
    },

    {
      id: "2",
      position: { x: 400, y: 100 },
      data: { label: "Credential Theft" }
    },

    {
      id: "3",
      position: { x: 700, y: 100 },
      data: { label: "Admin Access" }
    },

    {
      id: "4",
      position: { x: 1000, y: 100 },
      data: { label: "Data Breach" }
    }
  ];

  const edges = [
    {
      id: "e1-2",
      source: "1",
      target: "2"
    },

    {
      id: "e2-3",
      source: "2",
      target: "3"
    },

    {
      id: "e3-4",
      source: "3",
      target: "4"
    }
  ];

  return (
    <div
      style={{
        height: 500,
        background: "#111827",
        borderRadius: 12
      }}
    >
      <ReactFlow
        nodes={nodes}
        edges={edges}
        fitView
      />
    </div>
  );
}