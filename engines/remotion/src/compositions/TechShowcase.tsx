import React from "react";
import { AbsoluteFill, interpolate, spring, useCurrentFrame, useVideoConfig } from "remotion";
import { KineticText } from "../components/KineticText";
import { GlowCard } from "../components/GlowCard";
import { ParticleField } from "../components/ParticleField";

interface TechShowcaseProps {
  title: string;
  subtitle: string;
  badgeText: string;
}

export const TechShowcase: React.FC<TechShowcaseProps> = ({
  title,
  subtitle,
  badgeText,
}) => {
  const frame = useCurrentFrame();
  const { fps, width, height } = useVideoConfig();
  const isVertical = height > width;

  const badgeEntrance = spring({
    frame: frame - 5,
    fps,
    config: { damping: 10, mass: 0.5, stiffness: 100 },
  });

  const progressBar = interpolate(frame, [0, 180], [0, 100], {
    extrapolateRight: "clamp",
  });

  return (
    <AbsoluteFill
      style={{
        background: "linear-gradient(145deg, #090d16 0%, #0f172a 50%, #1e1b4b 100%)",
        color: "#ffffff",
        fontFamily: "system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif",
        overflow: "hidden",
        display: "flex",
        flexDirection: "column",
        justifyContent: "space-between",
        alignItems: "center",
        padding: isVertical ? "160px 48px 100px" : "80px 48px 60px",
      }}
    >
      <ParticleField count={40} />

      {/* Top Section */}
      <div style={{ display: "flex", flexDirection: "column", alignItems: "center", gap: 24, zIndex: 2 }}>
        <div
          style={{
            transform: `scale(${badgeEntrance})`,
            background: "rgba(30, 58, 138, 0.7)",
            border: "1px solid #60a5fa",
            borderRadius: 9999,
            padding: "8px 24px",
            fontSize: 20,
            fontWeight: 700,
            letterSpacing: "0.08em",
            color: "#93c5fd",
            boxShadow: "0 0 20px rgba(96, 165, 250, 0.4)",
          }}
        >
          {badgeText}
        </div>

        <KineticText text={title} delay={15} fontSize={isVertical ? 72 : 84} />

        <div
          style={{
            fontSize: isVertical ? 28 : 32,
            color: "#94a3b8",
            textAlign: "center",
            maxWidth: 700,
          }}
        >
          {subtitle}
        </div>
      </div>

      {/* Center Feature Card */}
      <div style={{ width: "100%", zIndex: 2 }}>
        <GlowCard
          delay={40}
          title="Ultra-Smooth Physics"
          subtitle="Spring Interpolation • Zero Dependencies"
          features={[
            "⚡ Streaming Raw Frames Directly to FFmpeg",
            "🎨 100% Code-Driven Custom Visual Effects",
            "📱 Multi-Format: 9:16 Vertical, 16:9 Landscape, 1:1 Square",
          ]}
        />
      </div>

      {/* Bottom Progress Bar */}
      <div
        style={{
          width: "80%",
          height: 6,
          background: "rgba(30, 41, 59, 0.8)",
          borderRadius: 3,
          overflow: "hidden",
          zIndex: 2,
        }}
      >
        <div
          style={{
            width: `${progressBar}%`,
            height: "100%",
            background: "linear-gradient(90deg, #38bdf8, #a855f7)",
            borderRadius: 3,
          }}
        />
      </div>
    </AbsoluteFill>
  );
};
