### 网络介绍
初始网络中有m0个0度节点，每个时刻引入一个新节点，每个新结点引入m条边与之前的节点相连，连接概率与度分布有关。共生成t个新节点。
因此生成网络有m0+t个结点、t*m条边.
### 输入参数
m:每个新节点引入的边数
m0:初始时刻结点数
t:网络生长时间
示例：
python3 BA_model.py --edgelist edgelist --m m --m0 m0 --t t