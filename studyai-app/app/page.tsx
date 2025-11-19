import styles from "@/app/home.module.css";
import Gradient from "@/components/gradient/gradient";
import Sidebar from "@/components/sidebar/sidebar";

export default function Home() {
  return (
    <main id={styles.main}>
      <Sidebar/>
      <div id={styles.container}>
        <div id={styles.search}>
          
        </div>
        <Gradient/>
      </div>
    </main>
  );
}
