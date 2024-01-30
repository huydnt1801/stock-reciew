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
    // axios
    //   .get(`${process.env.NEXT_PUBLIC_BE_URL}/api/v1/news${pathname}`)
    //   .then((res) => {
    //     setData(res.data);
    //   });
    setData({"_id":"65ac6cc3c3731323ffcab8d4","event_time":1705795200000,"message":"Bản tin: Tình hình tiền ảo giữ nguyên cặp mã tiền ảo\n\nTrong giờ qua, giá các cặp mã tiền ảo đã có những biến động nhất định. Đầu tiên, giá DOGEUSDT đã tăng 1.8% từ 0.08777 lên 0.08935. Trong khoảng thời gian từ 0:45 đến 0:46, DOGEUSDT tiếp tục tăng 0.46% với volume trung bình cao nhất đạt 3896007.0/phút. Tuy nhiên, từ 0:51 đến 0:58, DOGEUSDT đã giảm 0.8% với volume trung bình cao nhất là 4113810.6/phút.\n\nTrong khi đó, giá BTCUSDT đã giảm 0.12% từ 41696.05 xuống 41645.98 trong giờ qua. Tương tự, giá ETHUSDT cũng giảm 0.25% từ 2472.02 xuống 2465.78. Giá SHIBUSDT cũng không ngoại lệ khi giảm 0.31% từ 9.68e-06 xuống 9.65e-06 trong khoảng thời gian tương tự. Tuy nhiên, từ 0:45 đến 0:46, SHIBUSDT đã tăng 0.31% với volume trung bình cao nhất đạt 3100387126.0/phút. Nhưng từ 0:50 đến 0:57, giá SHIBUSDT lại giảm 0.31% với volume trung bình cao nhất là 2609441523.83/phút.\n\nTrong khi đó, giá BNBUSDT đã tăng 0.13% từ 317.3 lên 317.7 trong giờ qua. Tuy nhiên, giá XRPUSDT đã giảm 0.16% từ 0.5534 xuống 0.5525. Giá SOLUSDT cũng không có sự thay đổi tích cực khi giảm 0.8% từ 92.88 xuống 92.14. Cuối cùng, giá ADAUSDT cũng giảm 0.43% từ 0.5159 xuống 0.5137 trong giờ qua. Tuy nhiên, từ 0:45 đến 0:49, ADAUSDT đã tăng 0.35% với volume trung bình cao nhất đạt 19159.58/phút. Nhưng từ 0:49 đến 0:59, giá ADAUSDT lại giảm 0.58% với volume trung bình cao nhất là 60380.71/phút.\n\nTổng kết, trong giờ qua, giá các cặp mã tiền ảo đã có những biến động khác nhau. Một số cặp mã tiền ảo như DOGEUSDT và BNBUSDT đã có sự tăng giá nhỏ, trong khi các cặp mã tiền ảo khác như BTCUSDT, ETHUSDT, SHIBUSDT, XRPUSDT, SOLUSDT và ADAUSDT đã giảm giá. Các biến động này cho thấy tình hình tiền ảo vẫn đang diễn ra một cách không ổn định và cần được theo dõi thêm trong thời gian tới."},{"_id":"65ac7ae7c3731323ffcab8dd","event_time":1705798800000,"message":"Bản tin về tình hình tiền ảo giữ nguyên cặp mã tiền ảo:\n\nTrong giờ qua, giá DOGEUSDT đã tăng 1.8% từ mức 0.08777 lên 0.08935. Tuy nhiên, từ 0:45 đến 0:46, giá DOGEUSDT chỉ tăng 0.46% với volume trung bình cao nhất đạt 3,896,007.0 DOGE/phút. Sau đó, từ 0:51 đến 0:58, giá DOGEUSDT đã giảm 0.8% với volume trung bình cao nhất đạt 4,113,810.6 DOGE/phút.\n\nTrong cùng thời gian, giá BTCUSDT đã giảm 0.12% từ mức 41,696.05 USDT xuống 41,645.98 USDT. Tương tự, giá ETHUSDT cũng giảm 0.25% từ mức 2,472.02 USDT xuống 2,465.78 USDT. Giá SHIBUSDT cũng không có sự thay đổi lớn khi giảm 0.31% từ mức 9.68e-06 USDT xuống 9.65e-06 USDT.\n\nTuy nhiên, từ 0:45 đến 0:46, giá SHIBUSDT đã tăng 0.31% với volume trung bình cao nhất đạt 3,100,387,126.0 SHIB/phút. Sau đó, từ 0:50 đến 0:57, giá SHIBUSDT đã giảm 0.31% với volume trung bình cao nhất đạt 2,609,441,523.83 SHIB/phút.\n\nTrong cùng thời gian, giá BNBUSDT đã tăng 0.13% từ mức 317.3 USDT lên 317.7 USDT. Trong khi đó, giá XRPUSDT đã giảm 0.16% từ mức 0.5534 USDT xuống 0.5525 USDT. Giá SOLUSDT cũng giảm 0.8% từ mức 92.88 USDT xuống 92.14 USDT. Giá ADAUSDT cũng không có sự thay đổi lớn khi giảm 0.43% từ mức 0.5159 USDT xuống 0.5137 USDT.\n\nTuy nhiên, từ 0:45 đến 0:49, giá ADAUSDT đã tăng 0.35% với volume trung bình cao nhất đạt 19,159.58 ADA/phút. Sau đó, từ 0:49 đến 0:59, giá ADAUSDT đã giảm 0.58% với volume trung bình cao nhất đạt 60,380.71 ADA/phút. Từ 1:45 đến 1:50, giá ADAUSDT tăng 0.14% với volume trung bình cao nhất đạt 60,512.2 ADA/phút. Từ 1:41 đến 1:48, giá ADAUSDT giảm 0.45% với volume trung bình cao nhất đạt 36,134.48 ADA/phút. Trong giờ qua, giá ADAUSDT cũng giảm 0.18% từ mức 0.5138 USDT xuống 0.5129 USDT.\n\nTừ 1:31 đến 1:41, giá BTCUSDT tăng 0.16% với volume trung bình cao nhất đạt 7.74 BTC/phút. Sau đó, từ 1:41 đến 1:47, giá BTCUSDT giảm 0.12% với volume trung bình cao nhất đạt 15.92 BTC/phút. Từ 1:45 đến 1:47, giá ETHUSDT tăng 0.03% với volume trung bình cao nhất đạt 457.66 ETH/phút. Từ 1:50 đến 1:53, giá ETHUSDT giảm 0.03% với volume trung bình cao nhất đạt 103.34 ETH/phút.\n\nTrong giờ qua, giá XRPUSDT giảm 0.05% từ mức 0.5525 USDT xuống 0.5522 USDT. Từ 1:5 đến 1:6, giá XRPUSDT tăng 0.13% với volume trung bình cao nhất đạt 441,478.0 XRP/phút. Từ 1:30 đến 1:33, giá XRPUSDT giảm 0.18% với volume trung bình cao nhất đạt 142,387.0 XRP/phút.\n\nTrong giờ qua, giá DOGEUSDT đã tăng 0.5% từ mức 0.08935 USDT lên 0.0898 USDT. Từ 1:48 đến 1:55, giá DOGEUSDT tăng 1.46% với volume trung bình cao nhất đạt 3,376,315.86 DOGE/phút. Sau đó, từ 1:55 đến 1:57, giá DOGEUSDT giảm 0.22% với volume trung bình cao nhất đạt 4,515,741.0 DOGE/phút.\n\nTừ 1:18 đến 1:19, giá SHIBUSDT tăng 0.31% với volume trung bình cao nhất đạt 5,710,977,068.0 SHIB/phút. Sau đó, từ 1:19 đến 1:22, giá SHIBUSDT giảm 0.31% với volume trung bình cao nhất đạt 2,995,501,540.5 SHIB/phút. Từ 1:44 đến 1:50, giá BNBUSDT tăng 0.25% với volume trung bình cao nhất đạt 497.84 BNB/phút. Từ 1:41 đến 1:46, giá BNBUSDT giảm 0.32% với volume trung bình cao nhất đạt 392.44 BNB/phút. Từ 1:45 đến 1:51, giá SOLUSDT tăng 0.33% với volume trung bình cao nhất đạt 2,104.81 SOL/phút. Từ 1:51 đến 1:56, giá SOLUSDT giảm 0.36% với volume trung bình cao nhất đạt 1,316.07 SOL/phút."})
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
