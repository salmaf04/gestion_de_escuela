// frontend/src/pages/notas/components/AddNotaForm.tsx
import { useContext, useState } from "react";
import { NotasContext } from "../NotasScreen.tsx";
import { NotaCreateAdapter } from "../adapters/NotaCreateAdapter.ts";

export default function AddNotaForm() {
    const { onAddTableItem, setShowModal } = useContext(NotasContext);
    const [teacher_id, setTeacherId] = useState('');
    const [student_id, setStudentId] = useState('');
    const [subject_id, setSubjectId] = useState('');
    const [note_value, setNoteValue] = useState(0);

    const handleSubmit = (e: React.FormEvent) => {
        e.preventDefault();
        const newNota = new NotaCreateAdapter({ teacher_id, student_id, subject_id, note_value });
        onAddTableItem!(newNota);
        setShowModal!(false);
    };

    return (
        <div className="modal">
            <form onSubmit={handleSubmit} className="form">
                <label>
                    Teacher ID:
                    <input type="text" value={teacher_id} onChange={(e) => setTeacherId(e.target.value)} required />
                </label>
                <label>
                    Student ID:
                    <input type="text" value={student_id} onChange={(e) => setStudentId(e.target.value)} required />
                </label>
                <label>
                    Subject ID:
                    <input type="text" value={subject_id} onChange={(e) => setSubjectId(e.target.value)} required />
                </label>
                <label>
                    Note Value:
                    <input type="number" value={note_value} onChange={(e) => setNoteValue(Number(e.target.value))} required />
                </label>
                <button type="submit">Add Note</button>
                <button type="button" onClick={() => setShowModal!(false)}>Cancel</button>
            </form>
        </div>
    );
}