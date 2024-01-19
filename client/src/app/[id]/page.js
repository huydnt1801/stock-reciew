"use client";
import axios from "axios";
import { usePathname } from "next/navigation";
import { useEffect, useState } from "react";
export default function Detail() {
  const pathname = usePathname();
  const [data, setData] = useState(null);
  const [date, setDate] = useState(null);
  const [interval, setInterval] = useState(null);
  useEffect(() => {
    axios
      .get(`${process.env.NEXT_PUBLIC_BE_URL}/api/v1/news${pathname}`)
      .then((res) => {
        setData(res.data);
      });
  }, [pathname]);
  useEffect(() => {
    if (!data) return;
    const now = Date.now();
    const date = new Date(data.event_time);
    setDate(date)
    let interval = Math.trunc((now - date) / (1000 * 3600));
    setInterval(interval)
  }, [data]);
  return (
    <>
      {(data && date && interval) ? (
        <div className="w-full max-w-5xl flex flex-col h-auto px-10 py-4">
          <div className="font-semibold text-2xl text-center">
            {`[${date.getHours()}:00 ${
              date.getDate() +
              "/" +
              (date.getMonth() + 1) +
              "/" +
              date.getFullYear()
            }]`}{" Bản tin thị trường"}
          </div>
          <div className="text-base mt-3 flex-1">
            {data.message.split("\n").map((line) => (
              <p style={{ textIndent: "25px" }}>{line}</p>
            ))}
          </div>
          <div>
            <div className="mt-2 text-sm float-right">
              🕝 {interval} giờ trước
            </div>
          </div>
        </div>
      ) : (
        <div>Loading...</div>
      )}
    </>
  );
}
