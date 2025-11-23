"use client";

import styles from "@/components/searchbar/searchbar_styles.module.css"
import { CSSProperties } from "@mui/material";
import { ChangeEvent, FormEvent, KeyboardEvent, useRef, useState } from "react";

interface SearchbarProps {
    width: string;
    placeholder: string;
    size: "small" | "large";
}

export default function Searchbar({width, placeholder, size} : SearchbarProps) {
    const textAreaRef = useRef<HTMLTextAreaElement | null>(null);

    let classNameFromSize;
    switch (size) {
        case "small":
            classNameFromSize = styles.small;
            break;
        case "large":
            classNameFromSize = styles.large;
            break;
    }

    function onChange(event: ChangeEvent<HTMLTextAreaElement>) {
        // Auto expand
        event.target.style.height = "0px";
        event.target.style.height = event.target.scrollHeight + "px";
    }

    return (
        <textarea 
            ref={textAreaRef} 
            id={styles.search_bar} 
            className={classNameFromSize} 
            onChange={onChange}
            placeholder={placeholder}
            style={{width: width}}
        />
    );  
}