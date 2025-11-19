"use client";

import styles from "@/components/sidebar/notebook/notebook_styles.module.css";
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';
import { useState } from "react";


interface NotebookProps {
    name: string;
}

export default function Notebook({name} : NotebookProps) {
    const [expanded, setExpanded] = useState<boolean>(false);

    return (
        <div id={styles.notebook}>
            <p className={styles.inline}>{name}</p>
            <KeyboardArrowRightIcon id={styles.arrow} className={styles.inline}/>
        </div>
    );
}