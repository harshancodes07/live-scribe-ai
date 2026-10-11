
import { useState } from "react";
import "./App.css";

function App() {
  const [file, setFile] = useState<File | null>(null);
  const [transcript, setTranscript] = useState("");
  const [answer, setAnswer] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleTranscribe() {
    if (!file) {
      setError("Please choose an audio file first.");
      return;
    }

    setLoading(true);
    setError("");
    setTranscript("");
    setAnswer("");

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/transcribe",
        {
          method: "POST",
          body: formData,
        }
      );

      if (!response.ok) {
        throw new Error(`Request failed: ${response.status}`);
      }

      const data = await response.json();
      setTranscript(data.transcript);
      setAnswer(data.answer);
    } catch (err) {
      setError(
        err instanceof Error ? err.message : "Something went wrong."
      );
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="app">
      <header>
        <p className="eyebrow">YOUR AI MEETING COMPANION</p>
        <h1>LiveScribe<span> AI</span></h1>
        <p className="subtitle">
          Turn conversations into clear, useful explanations.
        </p>
      </header>

      <section className="upload-card">
        <h2>Transcribe & Explain</h2>
        <p>Upload a meeting or lecture recording to get started.</p>

        <label className="file-picker">
          <input
            type="file"
            accept=".m4a,.mp3,.wav,.mp4,audio/*"
            onChange={(event) => {
              setFile(event.target.files?.[0] ?? null);
              setError("");
            }}
          />
          <span>{file ? file.name : "Choose an audio file"}</span>
        </label>

        <button onClick={handleTranscribe} disabled={loading}>
          {loading ? "Processing audio..." : "Transcribe & Explain"}
        </button>

        {loading && <p className="status">Whisper and Ollama are working...</p>}
        {error && <p className="error">{error}</p>}
      </section>

      {(transcript || answer) && (
        <section className="results">
          {transcript && (
            <article>
              <h2>Transcript</h2>
              <p>{transcript}</p>
            </article>
          )}

          {answer && (
            <article>
              <h2>AI Explanation</h2>
              <p className="answer">{answer}</p>
            </article>
          )}
        </section>
      )}

      <footer>LiveScribe AI · Local AI-powered assistance</footer>
    </main>
  );
}

export default App;
