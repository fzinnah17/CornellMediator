export const getTestMessage = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/test');
      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const data = await response.json();
      return data.message;
    } catch (error) {
      console.error(error);
      return "Error fetching data";
    }
  };
  