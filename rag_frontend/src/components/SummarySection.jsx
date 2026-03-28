import { useEffect, useState } from "react";
import { getSummary } from "../services/api";
import "./SummarySection.css";

function SummarySection({ documentId }) {

  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    if (!documentId) return;

    const fetchSummary = async () => {
      try {
        setLoading(true);

        const response = await getSummary(documentId);

        setSummary(response.summary);

      } catch (error) {
        console.error("Error fetching summary:", error);
      } finally {
        setLoading(false);
      }
    };

    fetchSummary();

  }, [documentId]);

  if (!documentId) return null;

  return (
    <div className="summary-container">

      <h2 className="summary-title">Document Summary</h2>

      {loading ? (
        <p>Generating summary...</p>
      ) : (
        <p className="summary-text">{summary}</p>
      )}

    </div>
  );
}

export default SummarySection;