import React from "react";
import './AboutUs.css';

function AboutUs() {
  return (
    <div className="about-us-container">
      <h1>About Our Project</h1>
      <p className="project-abstract">
        In the fast-paced world of e-commerce, where user trust is pivotal, the development of a comprehensive solution is essential to address challenges related to user reviews, pricing accuracy, and urgency tactics. Our multifaceted project comprises three integral modules designed to bolster the credibility and transparency of e-commerce platforms with the added enhancement of a user-friendly web interface developed using React.

        <ul>
          <li>
            <strong>Review-Authenticator:</strong> Utilizes web scraping and sentiment analysis to discern potentially manipulated or fake reviews on Flipkart. By categorizing reviews based on sentiment and upvote/downvote patterns, it delivers insights into the prevalence of fraudulent reviews, contributing to the maintenance of a fair and transparent review system.
          </li>
          <li>
            <strong>PriceAuthenticator:</strong> Employs Selenium for web scraping to scrutinize pricing accuracy and detect dark patterns, ensuring e-commerce platforms provide genuine and transparent pricing information.
          </li>
          <li>
            <strong>Urgency-Detector:</strong> Analyzes product pages for the presence of manipulated urgency tactics, checking the authenticity of displayed timers. Together, these modules offer a comprehensive solution for e-commerce platforms to enhance the trustworthiness of their reviews, pricing details, and urgency tactics.
          </li>
        </ul>

        This project not only identifies potential issues but also empowers businesses to take corrective actions, ultimately fostering a more trustworthy and transparent online shopping environment for users.
      </p>
    </div>
  );
}

export default AboutUs;
