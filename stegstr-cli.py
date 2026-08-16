
import argparse, json, sys
from stegstr_core import embed_dct_qim, detect_dct_qim

def main():
    p=argparse.ArgumentParser(description="Stegstr R CLI - AI Agent Ready")
    sub=p.add_subparsers(dest="cmd")
    post=sub.add_parser("post"); post.add_argument("content"); post.add_argument("--output", default="bundle.json")
    emb=sub.add_parser("embed"); emb.add_argument("cover"); emb.add_argument("-o", dest="out", required=True); emb.add_argument("--payload"); emb.add_argument("--encrypt", action="store_true"); emb.add_argument("--strength", default="high")
    det=sub.add_parser("detect"); det.add_argument("image"); det.add_argument("--json", action="store_true")
    args=p.parse_args()
    if args.cmd=="post":
        bundle={"kind":1,"content":args.content,"created_at": 1234567890}
        open(args.output,"w").write(json.dumps(bundle))
        print(json.dumps({"ok":True,"bundle":args.output}))
    elif args.cmd=="embed":
        payload=json.loads(open(args.payload[1:]).read()) if args.payload and args.payload.startswith("@") else {"content":"test"}
        res=embed_dct_qim(args.cover, payload, args.out)
        print(json.dumps(res))
    elif args.cmd=="detect":
        res=detect_dct_qim(args.image)
        print(json.dumps(res) if args.json else str(res))
    else:
        p.print_help()

if __name__=="__main__": main()
