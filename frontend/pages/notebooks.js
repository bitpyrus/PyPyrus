import { useState } from "react";
import axios from "axios";

export default function Notebook() {
  const [title, setTitle] = useState("");

  const createNotebook = async () => {
    await axios.post("http://localhost:8000/notebooks/create", { title });
    alert(`Notebook '${title}' created!`);
  };

  return (
    <div className="p-10">
      <h1 className="text-2xl font-bold">Create a Notebook</h1>
      <input
        type="text"
        placeholder="Notebook Title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        className="border p-2"
      />
      <button onClick={createNotebook} className="bg-blue-500 text-white p-2">
        Create
      </button>
    </div>
  );
}
