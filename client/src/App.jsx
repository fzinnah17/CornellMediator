import React from 'react';
import { Routes, Route } from 'react-router-dom';
import CornellMediator from './CornellMediator';


const App = () => {
  return (
    <div>
      <Routes>
        <Route path="/" element={<CornellMediator />} />
      </Routes>
    </div>
  );
};

export default App;
