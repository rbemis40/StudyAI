import styles from "@/components/sidebar/sidebar_styles.module.css";
import NotebookList from "@/components/sidebar/notebook_list/notebook_list";

export default function Sidebar() {
    return (
        <div id={styles.container}>
            <h2>Notebooks</h2>
            <input id={styles.search_bar} placeholder="Search for notebooks..."></input>
            <NotebookList/>
        </div>
    )
}