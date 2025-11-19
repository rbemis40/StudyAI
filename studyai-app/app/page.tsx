import styles from "@/app/home.module.css";
import Sidebar from "@/components/sidebar/sidebar";
import Image from "next/image";

export default function Home() {
  return (
    <main id={styles.main}>
      <Sidebar/>
      <div id={styles.container}>
        <div id={styles.search}>
          <h1>Hello World!</h1>
        </div>
        <Gradient/>
      </div>
    </main>
  );
}
