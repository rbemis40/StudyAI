"use client";

import styles from "@/components/sidebar/sidebar_styles.module.css";
import NotebookList from "@/components/sidebar/notebook_list/notebook_list";
import { ChangeEvent, useMemo, useState } from "react";
import { NotebookData } from "./notebook_list/notebook/notebook";
import { Trie, TrieData } from "@/utils/trie";

export default function Sidebar() {
    const [notebooks, setNotebooks] = useState<NotebookData[]>([
        {
            name: "English Notes",
            materials: ["Lecture 1", "Lecture 2", "Lecture 3"]
        },
        {
            name: "Science Notes",
            materials: ["Lecture 1", "Lecture 2", "Lecture 3"]
        },
        {
            name: "Many Many Notes",
            materials: Array.from({length: 100}).map((_, i) => `Lecture ${i+1}`)
        },
        {
            name: "Math Notes",
            materials: ["Notes 1", "Notes 2"]
        },
        {
            name: "Test",
            materials: ["Test 1", "Test 2"]
        }
    ]);

    const trie = useMemo(() => {
        return new Trie<NotebookData>(
            notebooks.map(notebook => ({
                name: notebook.name.toLowerCase(),
                value: notebook
            } as TrieData<NotebookData>))
        )
    }, []);

    function search(event: ChangeEvent<HTMLInputElement>) {
        setNotebooks(trie.search(event.target.value.toLowerCase()));
    }

    return (
        <div id={styles.container}>
            <h2>Notebooks</h2>
            <input id={styles.search_bar} onChange={search} placeholder="Search for notebooks..."></input>
            <NotebookList notebooks={notebooks}/>
        </div>
    )
}