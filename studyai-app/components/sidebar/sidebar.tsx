import styles from "@/components/sidebar/sidebar_styles.module.css";
import Notebook from "./notebook/notebook";

export default function Sidebar() {
    return (
        <div id={styles.container}>
            <h2>Notebooks</h2>
            <input id={styles.search_bar} placeholder="Search for notebooks..."></input>
            <div id={styles.notebooks}>
                <Notebook name="English Notes"/>
                <Notebook name="Science Notes"/>
                <Notebook name="Test"/>
            </div>
        </div>
    )
}