import React from "react";
import { interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";

interface GlowCardProps {
  delay?: number;
  title: string;
  subtitle: string;
  features: string[];
}

export const GlowCard: React.FC<GlowCardProps> = ({
  delay = 45,
  title,
  subtitle,
  features,
}) => {
  const frame = useCurrentFrame();
  const { fps } = useVideoConfig();

  const entrance = spring({
    frame: frame - delay,
    fps,
    config: { damping: 12, mass: 0.6, stiffness: 120 },
  });

  const opacity = interpolate(frame - delay, [0, 15], [0, 1], {
    extrapolateLeft: "clamp",
    extrapolateRight: "clamp",
  });

  return (
    <div
      style={{
        transform: `scale(${entrance})`,
        opacity,
        background: "rgba(15, 23, 42, 0.85)",
        backdropFilter: "blur(20px)",
        border: "2px solid rgba(129, 140, 248, 0.6)",
        borderRadius: 28,
        padding: "48px 40px",
        boxShadow: "0 25px 50px -12px rgba(0, 0, 0, 0.5), 0 0 40px rgba(99, 102, 241, 0.25)",
        color: "#ffffff",
        textAlign: "center",
        maxWidth: 750,
        margin: "0 auto",
      }}
    >
      <h2 style={{ fontSize: 44, margin: "0 0 12px 0", fontWeight: 800, color: "#f8fafc" }}>
        {title}
      </h2>
      <p style={{ fontSize: 24, margin: "0 0 28px 0", color: "#c084fc", fontWeight: 500 }}>
        {subtitle}
      </p>
      <div style={{ display: "flex", flexDirection: "column", gap: 14 }}>
        {features.map((item, idx) => (
          <div
            key={idx}
            style={{
              fontSize: 22,
              color: "#38bdf8",
              background: "rgba(30, 41, 59, 0.6)",
              padding: "12px 20px",
              borderRadius: 14,
              border: "1px solid rgba(56, 189, 248, 0.2)",
            }}
          >
            {item}
          </div>
        ))}
      </div>
    </div>
  );
};
