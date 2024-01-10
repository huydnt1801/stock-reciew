import { Inter } from "next/font/google";
import "./globals.css";

const inter = Inter({ subsets: ["latin"] });

export const metadata = {
  title: "Bản tin thị trường tiền điện tử",
  description: "Thông tin thị trường tiền điện tử cập nhật liên tục từng giờ",
};

export default function RootLayout({ children }) {
  return (
    <html lang="en">
      <body className={inter.className}>
        <div className="w-full h-14 flex flex-col items-center">
          <div className="w-full max-w-5xl flex h-full flex-row border-b py-8">
            <div className="flex flex-row items-center">
              <button className="w-10 h-10 flex border items-center justify-center outline-none">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  viewBox="0 0 24 24"
                  className="w-6 h-6"
                  fill="none"
                >
                  <path
                    d="M5 6H12H19M5 12H19M5 18H19"
                    stroke="#000000"
                    stroke-width="2"
                    stroke-linecap="round"
                  />
                </svg>
              </button>
            </div>
            <div className="flex-1 flex items-center justify-center">
              <span className="text-3xl font-bold text-center">
                Bản tin thị trường tiền điện tử
              </span>
            </div>
            <div className="flex flex-row-reverse items-center">
              <button className="w-10 h-10 flex items-center justify-center outline-none">
                <svg
                  xmlns="http://www.w3.org/2000/svg"
                  className="w-6 h-6"
                  viewBox="0 0 24 24"
                  fill="none"
                >
                  <path
                    d="M5 12H3M12 5V3M21 12H19M12 21V19M16.9496 16.9498L18.3638 18.364M5.63602 5.63608L7.05023 7.05029M16.9496 7.0502L18.3638 5.63599M5.63602 18.3639L7.05023 16.9497M15 12C15 13.6569 13.6569 15 12 15C10.3431 15 9 13.6569 9 12C9 10.3431 10.3431 9 12 9C13.6569 9 15 10.3431 15 12Z"
                    stroke="#000000"
                    stroke-width="2"
                    stroke-linecap="round"
                    stroke-linejoin="round"
                  />
                </svg>
              </button>
            </div>
          </div>
          {children}
        </div>
      </body>
    </html>
  );
}
