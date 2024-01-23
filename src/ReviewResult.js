import React from "react";

function ResultPage({ location }) {
    if (!location || !location.state) {
        return <div>Error: Result not available</div>;
    }

    const { state } = location;
    const { analysis_result } = state;

    return (
        <div>
            <h1>Review Result Page</h1>

            <h2>Analysis Result</h2>
            <p>{analysis_result}</p>
        </div>
    );
}

export default ResultPage;
