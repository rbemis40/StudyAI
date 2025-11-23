"use client";

import Notebook, { NotebookData } from "@/components/sidebar/notebook_list/notebook/notebook";
import styles from "@/components/sidebar/notebook_list/notebook_list_styles.module.css";
import { useState } from "react";

interface NotebookListProps {
    notebooks: NotebookData[];
}

export default function NotebookList({notebooks} : NotebookListProps) {
    const [expandedNotebook, setExpandedNotebook] = useState<number>(-1);

    function onRequestExpand(index: number) {
        setExpandedNotebook(index === expandedNotebook ? -1 : index);
    }

    return (
        <div id={styles.notebooks}>
            {notebooks.map(((data, i) =>
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