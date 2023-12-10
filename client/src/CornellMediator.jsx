import React from "react";
import "./style.css";

export const CornellMediator = () => {
    return (
        <div className="mediator-wrapper">
            <div className="content-section">
                <div className="main-container">
                    <div className="record-section">
                        <div className="record-button-layout">
                            <div className="record-label">Record</div>
                        </div>
                    </div>
                    <p className="masala-chai-text">
                        Let's dive in the essence of authentic Indian Masala chai, a desi way to brighten your mood
                    </p>
                    <div className="mood-section">
                        <div className="mood-point">
                            <div className="point-description">
                                <div className="point-layout">
                                    <div className="point-details" />
                                    <img className="point-image-main" alt="Point image" src="point-image.png" />
                                    <img className="point-decorative-image" alt="Point image" src="image.png" />
                                </div>
                            </div>
                        </div>
                        <div className="mood-point-additional">
                            <div className="point-item">
                                <p className="point-message">Had a bad day? Trying to stay calm?</p>
                                <div className="point-image-layout">
                                    <div className="point-image-group">
                                        <div className="additional-point-details" />
                                        <img className="point-image-secondary" alt="Point image" src="point-image-2.png" />
                                        <img className="point-image-tertiary" alt="Point image" src="point-image-3.png" />
                                    </div>
                                </div>
                            </div>
                            <div className="point-item-extended">
                                <p className="extended-point-text">Pissed off by the landlord? And don’t know what to say?</p>
                                <div className="extended-layout">
                                    <div className="extended-image-group">
                                        <div className="extended-point-details" />
                                        <img className="point-image-quaternary" alt="Point image" src="point-image-4.png" />
                                        <img className="point-image-quinary" alt="Point image" src="point-image-5.png" />
                                    </div>
                                </div>
                            </div>
                        </div>
                        <div className="point-details-wrapper">
                            <div className="point-description-extended">
                                <div className="additional-mood-layout">
                                    <div className="point-details-secondary" />
                                    <div className="point-details-tertiary">
                                        <div className="point-image-container">
                                            <img className="point-image-final" alt="Point image" src="point-image-7.png" />
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                    <div className="response-section">
                        <div className="response-button-layout">
                            <div className="response-label">Generate Response</div>
                        </div>
                    </div>
                    <div className="navigation-container">
                        <div className="user-profile">
                            <div className="user-image-layout">
                                <img className="user-avatar" alt="User circle" src="user-circle.png" />
                                <div className="user-name">Akshay Iyer</div>
                            </div>
                        </div>
                        <div className="nav-element">
                            <img className="nav-line" alt="Nav item line" src="nav-item-line.svg" />
                        </div>
                        <p className="brand-logo">
                            <span className="brand-name">Cornell</span>
                            <span className="mediator-name">Mediator</span>
                        </p>
                    </div>
                </div>
                <img className="banner-image" alt="Banner content" src="banner-content-container.png" />
            </div>
        </div>
    );
}