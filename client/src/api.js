export const sendAudioToBackend = async (audioData) => {
    try {
      const formData = new FormData();
      formData.append('file', audioData);
  
      const response = await fetch('http://localhost:7860/api/predict/', {
        method: 'POST',
        body: formData,
      });
  
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
  
      const data = await response.json();
      return data;
    } catch (error) {
      console.error('Error in sending audio to backend:', error);
      return null;
    }
  };
  