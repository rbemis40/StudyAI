import type { Metadata } from "next";
import "@/app/global.css";

export const metadata: Metadata = {
  title: "ThreeRing AI",
  description: "Search and manage your notes faster than ever",
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <body>{children}</body>
    </html>
  );
}
