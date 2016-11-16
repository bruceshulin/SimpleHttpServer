using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Net;
using System.Text;
using System.Threading;

namespace Bend.Util
{
    public class HttpRequest
    {
        string uri = "http://192.168.60.128";
        public string httpRepuest(string address)
        {
            List<byte[]> listByte = new List<byte[]>();
            uri += address;
            HttpWebRequest request = HttpWebRequest.Create(uri) as HttpWebRequest;
            request.Method = "GET";                            //请求方法
            request.Timeout = 30000;
            request.ProtocolVersion = new Version(1, 1);   //Http/1.1版本

            HttpWebResponse response = request.GetResponse() as HttpWebResponse;
            Thread.Sleep(1000);
            //如果主体信息不为空，则接收主体信息内容
            if (response.ContentLength <= 0)
                return null;
            //接收响应主体信息
            using (Stream stream = response.GetResponseStream())
            {
                int totalLength = (int)response.ContentLength;
                int numBytesRead = 0;
                byte[] bytescount = new byte[totalLength + 1024];
                //通过一个循环读取流中的数据，读取完毕，跳出循环
                while (numBytesRead < totalLength)
                {
                    
                    int num = stream.Read(bytescount, numBytesRead, 1024);  //每次希望读取1024字节
                    if (num == 0)   //说明流中数据读取完毕
                        break;
                    numBytesRead += num;
                }
                
                //将接收到的主体数据显示到界面
                string content = Encoding.UTF8.GetString(bytescount);
                return content;
            }

        }

        static public byte[] ByteArrayAdd(List<byte[]> list)
        {
            using (System.IO.MemoryStream ms = new System.IO.MemoryStream())
            {
                foreach (var itembyte in list)
                {
                    ms.Write(itembyte, 0, itembyte.Length);
                }
                return ms.ToArray();
            }
        }



    }
}
