"use client";

import Grow from "@/components/animation/grow";
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
    const [visibility, setVisibility] = useState<"visible" | "hidden" | "growing" | "shrinking">("hidden");

    useEffect(() => {
        if (expanded && visibility !== "visible") {
            setVisibility("growing");
        }

        if (!expanded && visibility !== "hidden") {
            setVisibility("shrinking");
        }
    }, [expanded]);

    function onAnimComplete(mode: string) {
        switch (mode) {
            case "shrinking":
                setVisibility("hidden"); // The notebook was collaped, so it doesn't need to be in the DOM
                break;
            case "growing":
                setVisibility("visible");
                break;
        }
    }

    return (
        <div>
            <div id={styles.notebook} onClick={() => onRequestExpand()}>
                <p className={`unselectable ${styles.inline}`}>{data.name}</p>
                <KeyboardArrowRightIcon id={styles.arrow} className={`${styles.inline} ${(visibility === "growing" || visibility === "visible") ? styles.expanded_arrow : styles.unexpanded_arrow}`}/>
            </div>
            {visibility !== "hidden" && (<Grow duration={100} mode={visibility === "shrinking" ? "shrink" : "grow"} onComplete={onAnimComplete}>
                <div id={styles.materials}>
                    {data.materials.map(name => <p key={name}>{name}</p>)}
                </div>
            </Grow>)}
        </div>
    );
}