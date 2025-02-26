import React, { useState } from 'react';

function App() {
    const [prompt, setPrompt] = useState('');
    const [generatedCode, setGeneratedCode] = useState('');

    const handleGenerate = async () => {
        const response = await fetch('http://127.0.0.1:5000/generate-code', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ prompt })
        });

        const data = await response.json();
        setGeneratedCode(data.generated_code || "Error generating code.");
    };

    return (
        <div style={{ padding: '20px' }}>
            <h1>Appfodev CodeBot MVP</h1>
            <textarea 
                rows="3" 
                placeholder="Enter your prompt..." 
                value={prompt} 
                onChange={(e) => setPrompt(e.target.value)}
                style={{ width: '100%', padding: '10px' }}
            />
            <button onClick={handleGenerate}>Generate Code</button>
            <pre>{generatedCode}</pre>
        </div>
    );
}

export default App;
