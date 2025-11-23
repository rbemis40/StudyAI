import styles from "@/app/home.module.css";
import Gradient from "@/components/gradient/gradient";
import Searchbar from "@/components/searchbar/searchbar";
import Sidebar from "@/components/sidebar/sidebar";

export default function Home() {


  return (
    <main id={styles.main}>
      <Sidebar/>
      <div id={styles.container}>
        <div id={styles.search}>
          <h1>Get started searching your Science Notes...</h1>
          <Searchbar width="750px" size="large" placeholder="Enter your search..."/>
        </div>
        <Gradient/>
      </div>
    </main>
  );
}
