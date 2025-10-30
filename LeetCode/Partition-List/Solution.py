1<3:smaller
smaller:0->1->4->3->2->5->2
greater:0
-------
4>=3: greater
smaller:0->1->4->3->2->5->2
greater:0->4->3->2->5->2
-------
3>=3: greater
smaller:0->1->4->3->2->5->2
greater:0->4->3->2->5->2
-------
2<3:smaller
smaller:0->1->2->5->2
greater:0->4->3->2->5->2
-------
5>=3: greater
smaller:0->1->2->5->2
greater:0->4->3->5->2
-------
2<3:smaller
smaller:0->1->2->2
greater:0->4->3->5->2
-------
ans:
1->2->2->4->3->5