import React from "react";
import { useLocation } from "react-router-dom";
import './Resultpage.css';
import { Link } from "react-router-dom";

function Resultpage() {
    const location = useLocation();
    const result = location.state;
    const timerResult = result ? JSON.parse(result.timer_result) : null;
    const priceDifference = result.price_info["Maximum Retail Price"] - result.price_info["Special Price"];
    const totalLegit = result.analysis_result.legitimate_positive+result.analysis_result.legitimate_negative;
    const totalReviews = result.analysis_result.legitimate_positive+result.analysis_result.legitimate_negative+result.analysis_result.fake_negative+result.analysis_result.fake_positive;

    const isDarkPattern = priceDifference === result.price_info["Discount Amount"];

    return (
        <div className="result-container">
            <div className="result-cards-container">
                {result && (
                    <>
             
                        {result.analysis_result && (
                            <div className="result-card price-info-card">
                                <h3>Review Results</h3>
                                <ul>
                                    <div className="highlightGreenH3">{totalLegit}</div>
                                    out of <strong>{totalReviews}</strong>
                                    <hr></hr>
                                    <li><strong>Total Legitimate Positive Reviews:</strong> {result.analysis_result.legitimate_positive}</li>
                                    <li><strong>Total Legitimate Negative Reviews:</strong> {result.analysis_result.legitimate_negative}</li>
                                    <hr></hr>
                                    <li><strong>Total Fake Positive Reviews:</strong> {result.analysis_result.fake_positive}</li>
                                    <li><strong>Total Fake Negative Reviews:</strong> {result.analysis_result.fake_negative}</li>
                                </ul>
                            </div>
                        )}

                        {result.price_info && (
                            <div className="result-card price-info-card">
                                <h3>Price Information</h3>
                                <ul>
                                    <li><strong>Given Discount Percentage:</strong> <div className="highlightRed">{result.price_info["Given Discount Percentage"]}</div></li>
                                    <li><strong>Actual Discount Percentage:</strong> <div className="highlightGreen">{parseInt(result.price_info["Discount Percentage"])}</div></li>
                                    <hr/>
                                    <li><strong>Given Discount Amount:</strong> <div className="highlightRed">{priceDifference}</div></li>
                                    <li><strong>Actual Discount Amount:</strong> <div className="highlightGreen">{result.price_info["Discount Amount"]}</div></li>
                                    {isDarkPattern ? (
                                        <li><div className="highlightGreen"><h2>No dark pattern found</h2></div></li>
                                    ) : null}
                                </ul>
                            </div>
                        )}

                        {timerResult && (
                            <div className="result-card timer-info-card">
                                <h3>Timer Information</h3>
                                <div>
                                    <p><strong>Initial Timer:</strong> {timerResult.initial_time}</p>
                                    {timerResult.updated_time && (
                                        <p><strong>Updated Timer:</strong> {timerResult.updated_time}</p>
                                    )}
                                    <p><strong>Result:</strong> <div className="highlightGreen"> {timerResult.result}</div></p>
                                </div>
                            </div>
                        )}
                    </>
                )}
            </div>
        </div>
    );
}

export default Resultpage;
