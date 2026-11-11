import React from "react";
import { Composition } from "remotion";
import { TechShowcase } from "./compositions/TechShowcase";

export const RemotionRoot: React.FC = () => {
  return (
    <>
      {/* 9:16 Vertical Video (Shorts / Reels / TikTok) */}
      <Composition
        id="TechShowcaseVertical"
        component={TechShowcase}
        durationInFrames={180}
        fps={30}
        width={1080}
        height={1920}
        defaultProps={{
          title: "NEXT-GEN MOTION",
          subtitle: "Code-driven video animations at 60 FPS",
          badgeText: "MOTION CRAFT ENGINE v1.0",
        }}
      />

      {/* 16:9 Landscape Video (YouTube / Desktop) */}
      <Composition
        id="TechShowcaseLandscape"
        component={TechShowcase}
        durationInFrames={180}
        fps={30}
        width={1920}
        height={1080}
        defaultProps={{
          title: "NEXT-GEN MOTION",
          subtitle: "Code-driven video animations at 60 FPS",
          badgeText: "MOTION CRAFT ENGINE v1.0",
        }}
      />
    </>
  );
};
