"use client";

import { PropsWithChildren, useEffect, useRef, useState } from "react";

interface GrowProps extends PropsWithChildren {
    duration: number; // In ms
    mode: "grow" | "shrink";
    onComplete: (mode: "grow" | "shrink") => void;
}

export default function Grow({duration, mode, onComplete, children} : GrowProps) {
    const [height, setHeight] = useState(0);

    const containerRef = useRef<null | HTMLDivElement>(null);
    const sizeRef = useRef<null | HTMLDivElement>(null);

    let animationId: number;

    useEffect(() => {
        const rect = sizeRef.current!.getBoundingClientRect();
        const desiredHeight = mode === "grow" ? rect.height : 0;
        const dHeightPerMs = (desiredHeight - height) / duration;

        const lastTime = performance.now();
        const animate = (curTime: DOMHighResTimeStamp) => {
            const dTime = curTime - lastTime;
            
            const newHeight = height + (dTime * dHeightPerMs);
            if ((mode === "grow" && newHeight >= desiredHeight) || (mode === "shrink" && newHeight <= desiredHeight)) {
                setHeight(desiredHeight);
                onComplete(mode);
                return;
            }

            setHeight(newHeight);
            animationId = requestAnimationFrame(animate);
        };

        animationId = requestAnimationFrame(animate);

        return () => cancelAnimationFrame(animationId);
    }, [mode, containerRef, sizeRef]);

    return (
        <div ref={containerRef} style={{overflow: "hidden", height: height}}>
            <div ref={sizeRef}>
                {children}
            </div>
        </div>
    );
}