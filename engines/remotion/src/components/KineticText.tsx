import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

interface KineticTextProps {
  text: string;
  delay?: number;
  fontSize?: number;
}

export const KineticText: React.FC<KineticTextProps> = ({
  text,
  delay = 15,
  fontSize = 72,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const words = text.split(" ");

  return (
    <div
      style={{
        display: "flex",
        flexWrap: "wrap",
        justifyContent: "center",
        gap: "16px",
      }}
    >
      {words.map((word, wIdx) => {
        const wordDelay = delay + wIdx * 6;
        const progress = spring({
          frame: frame - wordDelay,
          fps,
          config: { damping: 12, mass: 0.5, stiffness: 140 },
        });

        const opacity = interpolate(frame - wordDelay, [0, 8], [0, 1], {
          extrapolateLeft: "clamp",
          extrapolateRight: "clamp",
        });

        const translateY = interpolate(progress, [0, 1], [40, 0]);

        return (
          <span
            key={wIdx}
            style={{
              fontSize,
              fontWeight: 900,
              color: "#ffffff",
              textShadow: "0 0 35px rgba(255,255,255,0.4), 0 0 70px rgba(56, 189, 248, 0.4)",
              letterSpacing: "0.04em",
              display: "inline-block",
              transform: `translateY(${translateY}px) scale(${progress})`,
              opacity,
            }}
          >
            {word}
          </span>
        );
      })}
    </div>
  );
};
