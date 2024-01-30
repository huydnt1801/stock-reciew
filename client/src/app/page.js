"use client";
import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/20/solid";
import React, { useEffect, useState } from "react";
import axios from "axios";
import Link from "next/link";
export default function Home() {
  const [data, setData] = useState([]);
  const [data2, setData2] = useState([]);
  useEffect(() => {
    fetch("/news.json")
      .then(
        (
          res //`${process.env.NEXT_PUBLIC_BE_URL}/api/v1/news`
        ) => res.json()
      )
      .then((res) => {
        let x = res.reverse()
        setData(x.slice(0, 4));
        setData2(x.slice(4, 8));
      });
  }, []);
  return (
    <>
      <div className="w-full max-w-5xl flex flex-row mt-4 h-auto">
        <div className="w-1/2 flex flex-col h-auto">
          {data.map((item) => {
            const now = Date.now();
            const date = new Date(item.event_time);
            let interval = Math.trunc((now - date) / (1000 * 3600));
            return (
              <Link
                key={item._id}
                href={`/${item._id}`}
                className="w-full relative"
              >
                <div
                  className="absolute w-20 h-28 top-4 flex flex-col rounded-lg overflow-hidden"
                  style={{ backgroundColor: "#2b9797" }}
                >
                  <div className="flex-1 flex items-center justify-center text-white font-bold text-5xl">
                    {date.getHours()}
                  </div>
                  <div
                    className="w-full h-10 flex items-center justify-center text-white font-bold text-sm"
                    style={{ backgroundColor: "#01302a" }}
                  >
                    {date.getDate() +
                      "/" +
                      (date.getMonth() + 1) +
                      "/" +
                      date.getFullYear()}
                  </div>
                </div>
                <div
                  className="ml-10 pl-16 pr-4 text-white py-4"
                  style={{ backgroundColor: "#006464" }}
                >
                  <div className="font-semibold text-xl">{item.title}</div>
                  <div className="text-sm mt-3 flex-1">
                    {item.message.slice(0, 200)}...
                  </div>
                  <div className="mt-2 text-xs text-gray-200">
                    🕝 {interval} giờ trước
                  </div>
                </div>
              </Link>
            );
          })}
        </div>
        <div className="w-1/2 ml-6 mb-10 flex flex-col">
          {data2.map((item, idx) => {
            const now = Date.now();
            const date = new Date(item.event_time);
            let interval = Math.trunc((now - date) / (1000 * 3600));
            return (
              <div key={item._id} className="w-full relative">
                <div
                  className="absolute w-20 h-28 top-4 flex flex-col rounded-lg overflow-hidden"
                  style={{ backgroundColor: "#2b9797" }}
                >
                  <div className="flex-1 flex items-center justify-center text-white font-bold text-5xl">
                    {date.getHours()}
                  </div>
                  <div
                    className="w-full h-10 flex items-center justify-center text-white font-bold text-sm"
                    style={{ backgroundColor: "#01302a" }}
                  >
                    {date.getDate() +
                      "/" +
                      (date.getMonth() + 1) +
                      "/" +
                      date.getFullYear()}
                  </div>
                </div>
                <div
                  className={`ml-10 pl-16 pr-4 text-black py-4 border-l border-r border-gray-400 ${
                    idx === data2.length - 1
                      ? "border-b"
                      : idx === 0 && "border-t"
                  }`}
                  style={{ backgroundColor: "#ffffff" }}
                >
                  <div className="font-semibold text-xl">{item.title}</div>
                  <div className="text-sm mt-3 flex-1">
                    {item.message.slice(0, 200)}...
                  </div>
                  <div className="mt-2 text-xs text-gray-600">
                    🕝 {interval} giờ trước
                  </div>
                </div>
              </div>
            );
          })}
        </div>
      </div>
      <div className="flex items-center justify-between border-t border-gray-200 bg-white px-4 py-3 sm:px-6">
        <div className="flex flex-1 justify-between sm:hidden">
          <a
            href="#"
            className="relative inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
          >
            Previous
          </a>
          <a
            href="#"
            className="relative ml-3 inline-flex items-center rounded-md border border-gray-300 bg-white px-4 py-2 text-sm font-medium text-gray-700 hover:bg-gray-50"
          >
            Next
          </a>
        </div>
        <div className="hidden sm:flex sm:flex-1 sm:items-center sm:justify-between">
          <div>
            <nav
              className="isolate inline-flex -space-x-px rounded-md shadow-sm"
              aria-label="Pagination"
            >
              <a
                href="#"
                className="relative inline-flex items-center rounded-l-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                <span className="sr-only">Previous</span>
                <ChevronLeftIcon className="h-5 w-5" aria-hidden="true" />
              </a>
              {/* Current: "z-10 bg-indigo-600 text-white focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600", Default: "text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:outline-offset-0" */}
              <a
                href="#"
                aria-current="page"
                className="relative z-10 inline-flex items-center bg-indigo-600 px-4 py-2 text-sm font-semibold text-white focus:z-20 focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-indigo-600"
              >
                1
              </a>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                2
              </a>
              <a
                href="#"
                className="relative hidden items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0 md:inline-flex"
              >
                3
              </a>
              <span className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-700 ring-1 ring-inset ring-gray-300 focus:outline-offset-0">
                ...
              </span>
              <a
                href="#"
                className="relative hidden items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0 md:inline-flex"
              >
                8
              </a>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                9
              </a>
              <a
                href="#"
                className="relative inline-flex items-center px-4 py-2 text-sm font-semibold text-gray-900 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                10
              </a>
              <a
                href="#"
                className="relative inline-flex items-center rounded-r-md px-2 py-2 text-gray-400 ring-1 ring-inset ring-gray-300 hover:bg-gray-50 focus:z-20 focus:outline-offset-0"
              >
                <span className="sr-only">Next</span>
                <ChevronRightIcon className="h-5 w-5" aria-hidden="true" />
              </a>
            </nav>
          </div>
        </div>
      </div>
    </>
  );
}
