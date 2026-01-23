import { useEffect, useState } from "react";
import axios from "axios";
import { ICategory } from "../types/ICategory";

const API = import.meta.env.VITE_API_BASE_URL + "/api/categories/";

const CategoriesPage = () => {
    const [categories, setCategories] = useState<ICategory[]>([]);
    const [name, setName] = useState("");
    const [description, setDescription] = useState("");
    const [image, setImage] = useState<File | null>(null);

    const loadCategories = async () => {
        const res = await axios.get(API);
        setCategories(res.data);
    };

    useEffect(() => {
        loadCategories();
    }, []);

    const createCategory = async () => {
        const formData = new FormData();
        formData.append("name", name);
        formData.append("description", description);
        if (image) formData.append("image", image);

        await axios.post(API, formData, {
            headers: { "Content-Type": "multipart/form-data" }
        });

        setName("");
        setDescription("");
        setImage(null);
        loadCategories();
    };

    const deleteCategory = async (id?: number) => {
        await axios.delete(API + id + "/");
        loadCategories();
    };

    return (
        <div style={{ padding: 40 }}>
            <h2>Categories CRUD</h2>

            <input
                placeholder="Name"
                value={name}
                onChange={(e) => setName(e.target.value)}
            />
            <br /><br />

            <textarea
                placeholder="Description"
                value={description}
                onChange={(e) => setDescription(e.target.value)}
            />
            <br /><br />

            <input
                type="file"
                onChange={(e) => setImage(e.target.files?.[0] || null)}
            />
            <br /><br />

            <button onClick={createCategory}>Create Category</button>

            <hr />

            {categories.map(cat => (
                <div key={cat.id} style={{ marginBottom: 20 }}>
                    <h3>{cat.name}</h3>
                    <p>{cat.description}</p>
                    <button onClick={() => deleteCategory(cat.id)}>
                        Delete
                    </button>
                </div>
            ))}
        </div>
    );
};

export default CategoriesPage;
