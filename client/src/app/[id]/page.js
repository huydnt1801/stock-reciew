import { ChevronLeftIcon, ChevronRightIcon } from "@heroicons/react/20/solid";
const data = {
  event: 1704963600000,
  title: "Bản tin thị trường",
  detai:
    "Trên thị trường tiền ảo, trong giờ qua, chứng kiến sự biến động nhẹ của các đồng tiền hàng đầu. Giá Bitcoin (BTCUSDT) đã tăng 0.2%, với mức cao nhất đạt 43020.01 và mức thấp nhất là 42784.13 trong khoảng thời gian từ 17:22 đến 17:55 vào ngày 14/12/2023. Chỉ số dòng tiền MFI cho BTCUSDT ở mức 42.3, còn chỉ số kỹ thuật RSI là 33.71 trong 14 giờ gần nhất.\nĐồng tiền điện tử khác, Terra (LUNAUSDT), ghi nhận giá cao nhất ở mức 0.9972 và giá thấp nhất là 0.9892 trong cùng một khoảng thời gian. Chỉ số MFI cho LUNAUSDT đạt 20.56, còn chỉ số RSI là 44.52 trong 14 giờ qua.\nEthereum (ETHUSDT) đã có biến động nhẹ, giảm 0.22% từ 17:55 đến 18:00 vào ngày 14/12/2023, với mức giá cao nhất là 2290.77 và mức thấp nhất là 2276.0. Đồng thời, chỉ số MFI cho ETHUSDT là 57.49 và chỉ số RSI là 47.49 trong 14 giờ gần nhất.\nĐối với Binance Coin (BNBUSDT), giá cao nhất đạt 252.8 và thấp nhất là 251.7. Biến động giá diễn ra trong thời gian ngắn, từ 17:27 đến 17:28, giá tăng 0.12%, sau đó từ 17:26 đến 17:28, giảm 0.12%. Chỉ số MFI cho BNBUSDT ở mức 42.15 và chỉ số RSI là 51.68 trong 14 giờ qua.\nXRP (XRPUSDT) ghi nhận giá cao nhất là 0.6326 và giá thấp nhất là 0.629 trong khoảng thời gian gần nhất. Chỉ số MFI cho XRPUSDT là 50.63 và chỉ số RSI là 49.13 trong 14 giờ qua.\nDogeCoin (DOGEUSDT) có mức giá cao nhất là 0.09758 và thấp nhất là 0.09663. Trong khoảng thời gian từ 17:33 đến 17:36, DOGEUSDT tăng 0.29% với mức volume trung bình cao nhất đạt 1804844.3333333333/phút. Chỉ số MFI cho DOGEUSDT đạt 47.02, còn chỉ số RSI là 31.07 trong 14 giờ qua.\nVề các cặp giao dịch giữa tiền ảo và Bitcoin, ETHBTC ghi nhận giá cao nhất là 0.05331 và thấp nhất là 0.05317. Trong khoảng thời gian từ 17:32 đến 17:41, ETHBTC tăng 0.13% với mức volume trung bình cao nhất là 32.42408888888889/phút. Chỉ số MFI cho ETHBTC là 94.6 và chỉ số RSI là 78.05 trong 14 giờ qua.\nBNBBTC có giá cao nhất là 0.005902 và thấp nhất là 0.005865. Trong khoảng thời gian từ 17:32 đến 17:35, BNBBTC tăng 0.1% với mức volume trung bình cao nhất là 300.02166666666665/phút. Chỉ số MFI cho BNBBTC là 44.22 và chỉ số RSI là 52.88 trong 14 giờ qua.\nVề SOLBTC, giá cao nhất là 0.0016933 và thấp nhất là 0.0016836. Đồng SOLBTC ghi nhận sự biến động lớn trong thời gian gần đây. Chỉ số MFI cho SOLBTC đạt 51.36 và chỉ số RSI là 63.81 trong 14 giờ qua.\nCuối cùng, đồng tiền SHIBUSDT có giá cao nhất là 1.012e-05 và thấp nhất là 1.003e-05 trong 14 giờ gần nhất. Chỉ số MFI cho SHIBUSDT đạt 69.53 và chỉ số RSI là 61.62.\nTình hình chung của thị trường tiền ảo trong thời gian gần đây vẫn ghi nhận sự biến động nhẹ với mức giá dao động và các chỉ số kỹ thuật không thay đổi đáng kể",
};
export default function Detail() {
  const now = Date.now();
  const date = new Date(data.event);
  let interval = Math.trunc((now - date) / (1000 * 3600));
  return (
    <>
      <div className="w-full max-w-5xl flex flex-col mt-4 h-auto p-10">
        <div className="font-semibold text-2xl text-center">
          {`[${date.getHours()}:00 ${
            date.getDate() +
            "/" +
            (date.getMonth() + 1) +
            "/" +
            date.getFullYear()
          }]`}{" "}
          {data.title}
        </div>
        <div className="text-base mt-3 flex-1">
          {data.detai.split("\n").map((line) => (
            <p style={{ textIndent: "25px" }}>{line}</p>
          ))}
        </div>
        <div>
          <div className="mt-2 text-sm float-right">
            🕝 {interval} giờ trước
          </div>
        </div>
      </div>
    </>
  );
}
