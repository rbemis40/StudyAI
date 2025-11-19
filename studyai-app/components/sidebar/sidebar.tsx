"use client";

import styles from "@/components/sidebar/sidebar_styles.module.css";
import KeyboardArrowRightIcon from '@mui/icons-material/KeyboardArrowRight';

export default function Sidebar() {
    return (
        <div id={styles.container}>
            <h2>Notebooks</h2>
            <input id={styles.search_bar} placeholder="Search for notebooks..."></input>
            <div id={styles.notebooks}>
                <p>English Notes</p>
                <p>Science Notes</p>
                <KeyboardArrowRightIcon></KeyboardArrowRightIcon>
            </div>
        </div>
    )
}