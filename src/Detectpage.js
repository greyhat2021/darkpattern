
import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import './Detectpage.css';

function Detectpage() {
    const [productUrl, setProductUrl] = useState('');
    const navigate = useNavigate();

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            const response = await fetch('http://localhost:7000/run_python_code', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ product_url: productUrl }),
            });

            if (!response.ok) {
                throw new Error('Failed to fetch');
            }

            const result = await response.json();

            if ('price_info' in result && 'timer_result' in result && 'analysis_result') {
                navigate('/result', { state: result });
            } else {
                console.error('Error:', 'Price info or timer result not available');
            }
        } catch (error) {
            console.error('Error fetching data:', error);
        }
    };

    return (
        <div className="detect-container">
            <div className="policy-container">
                <h1>FLIPKART'S PRIVACY POLICY</h1>
                <ol>
                    <li>Data Collection: Flipkart gathers user data, including preferences and transactions, for personalized services.</li>
                    <li>Types of Data: Collected information ranges from user preferences to sensitive data like PAN and credit details.</li>
                    <li>Data Usage: Flipkart utilizes data for personalized services, user behavior analysis, and improving overall customer experience.</li>
                    <li>Information Sharing: Personal information may be shared with internal entities, affiliates, and third parties for order fulfillment and marketing.</li>
                    <li>User Rights: Users can manage their data, withdraw consent, and review the Privacy Policy for updates. Consent is implicit in platform usage.</li>
                </ol>
            </div>
            <form id="form-section" onSubmit={handleSubmit}>
                <label>PROVIDE THE PRODUCT URL</label>
                <input
                    type="text"
                    id="product_url"
                    name="product_url"
                    className="product_url"
                    placeholder="Enter the URL"
                    value={productUrl}
                    onChange={(e) => setProductUrl(e.target.value)}
                    required
                />
                <br/>
                <input type="submit" value="GO" className="submit"/>
            </form>
        </div>
    );
}

export default Detectpage;





