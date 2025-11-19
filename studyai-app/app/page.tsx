import styles from "@/app/home.module.css";
import Image from "next/image";

export default function Home() {
  return (
    <main>
      <Image 
        src="/wip.jpg" 
        alt="Work in Progress"
        width={893}
        height={360}
        style={{display: "block", margin: "auto"}}
      />
    </main>
  );
}
