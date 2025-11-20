"use client";

import styles from "@/components/sidebar/notebook_list/notebook/notebook_styles.module.css";
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import { useEffect, useState } from "react";


interface NotebookProps {
    expanded: boolean;
    data: NotebookData;
    onRequestExpand: () => void;
}

export interface NotebookData {
    name: string;
    materials: string[];
}

export default function Notebook({data, expanded, onRequestExpand} : NotebookProps) {
    const [isExpanded, setIsExpanded] = useState<boolean>(expanded);

    useEffect(() => {
        setIsExpanded(expanded);
    }, [expanded]);

    return (
        <div>
            <div id={styles.notebook} onClick={() => onRequestExpand()}>
                <p className={`unselectable ${styles.inline}`}>{data.name}</p>
                <KeyboardArrowRightIcon id={styles.arrow} className={`${styles.inline} ${isExpanded ? styles.rotated : ''}`}/>
            </div>
            <div id={styles.materials}>
                {isExpanded && data.materials.map(name => <p key={name}>{name}</p>)}
            </div>
        </div>
    );
}