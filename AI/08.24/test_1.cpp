//+------------------------------------------------------------------+
//|RL agent base class                                               |
//+------------------------------------------------------------------+
class CRLAgent
    {
public:
                    CRLAgent(string,int,int,int,double, double);
                    ~CRLAgent(void);
    static int        agentIDs;

    void              updatePolicy(double,double&[]); //各取引の後に学習ポリシーを更新する
    void              updateReward();                 //取引終了後に報酬を更新する
    double            getTradeSignal(double&[]);      //学習したエージェントまたはランダムで取引シグナルを取得する
    int               trees;
    double            r;
    int               features;
    double            rferrors[], lastrferrors[];
    string            Name;