import React, { useState, useRef } from 'react';
import { sendAudioToBackend } from './api';
import './css/CornellMediator.css';

export const CornellMediator = () => {
    const [isRecording, setIsRecording] = useState(false);
    const [audioData, setAudioData] = useState(null);
    const [responseText, setResponseText] = useState('');
    const mediaRecorderRef = useRef(null);

    const startRecording = async () => {
        try {
            const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
            const mediaRecorder = new MediaRecorder(stream);
            mediaRecorderRef.current = mediaRecorder;
            let audioChunks = [];

            mediaRecorder.ondataavailable = (event) => {
                audioChunks.push(event.data);
            };

            mediaRecorder.onstop = () => {
                const audioBlob = new Blob(audioChunks, { type: 'audio/wav' });
                setAudioData(audioBlob);
            };

            mediaRecorder.start();
            setIsRecording(true);
        } catch (error) {
            console.error('Error starting recording:', error);
        }
    };

    const stopRecording = () => {
        mediaRecorderRef.current.stop();
        setIsRecording(false);
    };

    const handleGenerateResponse = async () => {
        if (audioData) {
            const response = await sendAudioToBackend(audioData);
            if (response) {
                setResponseText(response.data);
            }
        }
    };


    return (
        <div className="cornell-app">
            <nav className="app-navbar">
                <div className="logo">Logo</div>
                <div className="user-profile">
                    <img src="path-to-user-profile.jpg" alt="User" />
                    <span>Username</span>
                </div>
            </nav>
            <div className="content">
            <div className="buttons-container">
                {isRecording ? (
                    <button className="record-btn" onClick={stopRecording}>Stop Recording</button>
                ) : (
                    <button className="record-btn" onClick={startRecording}>Start Recording</button>
                )}
                <button className="generate-btn" onClick={handleGenerateResponse} disabled={!audioData}>Generate Response</button>
                <div className="response-box">{responseText}</div>
                </div>
            </div>
        </div>
    );
};
