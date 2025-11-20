"use client";

import Notebook, { NotebookData } from "@/components/sidebar/notebook_list/notebook/notebook";
import styles from "@/components/sidebar/notebook_list/notebook_list_styles.module.css";
import { useState } from "react";

export default function NotebookList() {
    const [expandedNotebook, setExpandedNotebook] = useState<number>(-1);

    function onRequestExpand(index: number) {
        setExpandedNotebook(index === expandedNotebook ? -1 : index);
        console.log(index);
    }

    const noteData: NotebookData[] = [
        {
            name: "English Notes",
            materials: ["Lecture 1", "Lecture 2", "Lecture 3"]
        },
        {
            name: "Science Notes",
            materials: ["Lecture 1", "Lecture 2", "Lecture 3"]
        },
        {
            name: "Test",
            materials: ["Test 1", "Test 2"]
        }
    ];

    return (
        <div id={styles.notebooks}>
            {noteData.map(((data, i) =>
                <Notebook 
                    key={data.name} 
                    expanded={i === expandedNotebook} 
                    onRequestExpand={() => onRequestExpand(i)}
                    data={data}
                />
            ))}
        </div>
    )
}