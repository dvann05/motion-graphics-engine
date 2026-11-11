import React, { useMemo } from "react";
import { useCurrentFrame } from "remotion";

export const ParticleField: React.FC<{ count?: number }> = ({ count = 35 }) => {
  const frame = useCurrentFrame();

  const particles = useMemo(() => {
    return Array.from({ length: count }).map((_, i) => ({
      x: (i * 37) % 100,
      y: (i * 53) % 100,
      speed: 0.2 + ((i * 13) % 10) * 0.08,
      size: 3 + ((i * 7) % 6),
      color:
        i % 3 === 0
          ? "rgba(56, 189, 248, 0.7)"
          : i % 3 === 1
          ? "rgba(168, 85, 247, 0.7)"
          : "rgba(236, 72, 153, 0.7)",
    }));
  }, [count]);

  return (
    <div
      style={{
        position: "absolute",
        top: 0,
        left: 0,
        right: 0,
        bottom: 0,
        overflow: "hidden",
        pointerEvents: "none",
      }}
    >
      {particles.map((p, idx) => {
        const currentY = (p.y - frame * p.speed * 0.4) % 100;
        const normalizedY = currentY < 0 ? currentY + 100 : currentY;

        return (
          <div
            key={idx}
            style={{
              position: "absolute",
              left: `${p.x}%`,
              top: `${normalizedY}%`,
              width: p.size,
              height: p.size,
              borderRadius: "50%",
              background: p.color,
              boxShadow: `0 0 ${p.size * 2}px ${p.color}`,
            }}
          />
        );
      })}
    </div>
  );
};
