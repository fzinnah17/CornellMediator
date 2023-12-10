import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import { CornellMediator } from './CornellMediator';

const App = () => {
  return (
    <Router>
      <div>
        <Routes>
          <Route path="/" element={<CornellMediator />} />
        </Routes>
      </div>
    </Router>
  );
};

export default App;
