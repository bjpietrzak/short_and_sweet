import React, { useState, ChangeEvent, KeyboardEvent } from 'react';
import axios from 'axios';

interface UrlInputProps {
  onUrlSubmitted: (appId: string) => void;
}

const UrlInput: React.FC<UrlInputProps> = ({ onUrlSubmitted }) => {
  const [url, setUrl] = useState<string>('');

  const handleUrlChange = (event: ChangeEvent<HTMLInputElement>) => {
    setUrl(event.target.value);
  };

  const handleKeyDown = async (event: KeyboardEvent<HTMLInputElement>) => {
    if (event.key === 'Enter') {
      try {
        const response = await axios.get(`http://0.0.0.0:7001/app_data/?url=${encodeURIComponent(url)}`);

        if (response.status === 200) {
            console.log(response.data)
          onUrlSubmitted(response.data.app_id);
        } else {
          console.error('Error sending URL:', response.statusText);
        }
      } catch (error) {
        console.error('Error sending URL:', error);
      }
    }
  };

  return (
    <div>
      <label htmlFor="urlInput">Enter URL:</label>
      <input
        type="text"
        id="urlInput"
        value={url}
        onChange={handleUrlChange}
        onKeyDown={handleKeyDown}
      />
    </div>
  );
};

export default UrlInput;
