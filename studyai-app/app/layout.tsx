import type { Metadata } from "next";
import "@/app/global.css";
import { Noto_Serif } from "next/font/google";

export const metadata: Metadata = {
  title: "ThreeRing AI",
  description: "Search and manage your notes faster than ever",
};

const noto_serif = Noto_Serif({
  subsets: ["latin"],
  style: ["normal"],
  weight: ["300", "400", "600"]
})

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en" className={noto_serif.className}>
      <body>{children}</body>
    </html>
  );
}
