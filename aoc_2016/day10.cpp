#include <iostream>
#include <sstream>
#include <map>
#include <fstream> 

using S = std::string;

S load_file(S name){
    std::ifstream text_file;
    text_file.open(name);
    if (!text_file) {
        std::cout << "Unable to open file: " << name << std::endl;
        exit(1); // terminate with error
    }

    std::stringstream txt_buff;
    txt_buff << text_file.rdbuf();

    return txt_buff.str();
}


std::vector<S> splitter(S payload, char delimiter)
{
    std::stringstream ss(payload);
    S token;
    std::vector<std::string> tokens;
    while (std::getline(ss, token, delimiter))
    {
        if (token == "")
            continue;

        tokens.push_back(token);
    }

    return tokens;
}

struct Bot
{
    S name = "";
    int high = 0, low = 0;

    Bot() {}

    Bot(S id)
    {
        name = id;
    }

    bool is_ready() const
    {
        return (high != 0 && low != 0);
    }

    void add(int v){
        if (high > v)
            low = v;
        else
        {
            low = high;
            high = v;
        }
    }

    void add(S value)
    {
        int v = std::stoi(value);
        this->add(v); 
    }

    bool check(int a, int b){
        if(a == high && b == low){
            return true; 
        }

        if(a == low && b == high){
            return true; 
        }

        return false;
    }

    void done(){
        low = 0;
        high = 0; 
    }
};

struct Link
{
    Bot *giver, *reciever_low, *reciever_high;
};

using BotMap = std::map<S, Bot>;

void dbg(BotMap *bots)
{
    std::cout << "\n=========== size: " << bots->size() << std::endl;
    for (auto x : *bots)
    {

        std::cout << "KEY name: " << x.first << std::endl;
        std::cout << "bot name: " << x.second.name << std::endl;
        std::cout << "high: " << x.second.high << std::endl;
        std::cout << "low: " << x.second.low << std::endl;
    }
}

void dbg_link(const Link &link){
    std::cout << "robot " << link.giver->name << " giving its chip lower ";
    std::cout << link.giver->low << " to: " << link.reciever_low->name; 
    std::cout << " giving its high one " << link.giver->high << " to: " << link.reciever_high->name ; 
    std::cout << std::endl;
}

void lazy_load(BotMap &bots, std::vector<S> names)
{
    for (auto name : names)
        if (!bots.count(name))
            bots[name] = {name};
}

void solve_puzzle_1(S ss, int a=2, int b=5)
{

    BotMap bots;
    auto lines = splitter(ss, '\n');
    std::vector<Link> links;

    for (auto line : lines)
    {
        auto tokens = splitter(line, ' ');
        S bot_name = "";

        if (tokens[0] == "value")
        {
            bot_name = "bot_" + tokens.back();
            auto value = tokens[1];

            lazy_load(bots, {bot_name});
            auto b = &bots[bot_name];
            b->add(value);
        }

        if (tokens[0] == "bot")
        {
            auto bot_name = "bot_" + tokens[1];
            auto type_1 = tokens[5];
            auto val_1 = tokens[6];
            auto val_2 = tokens.back();
            tokens.pop_back();
            auto type_2 = tokens.back();

            auto r1 = type_1 + "_" + val_1;
            auto r2 = type_2 + "_" + val_2;
            lazy_load(bots, {bot_name, r1, r2});

            auto giver = &bots[bot_name];
            auto br1 = &bots[r1];
            auto br2 = &bots[r2];
            links.push_back({giver, br1, br2});
        }
    }

    // dbg(&bots);

    while(true){
        bool jobs_remaining = false; 
        for (auto const &link : links)
        {
            if(link.giver->is_ready()){
                jobs_remaining = true;

                //dbg_link(link);
                if(link.giver->check(a,b)){
                    std::cout << link.giver->name << " has: " << a << ", " << b << " values ##";
                }

                link.reciever_low->add(link.giver->low);
                link.reciever_high->add(link.giver->high);
                link.giver->done();
            }
        }

        if(!jobs_remaining)
            break;
    }

    std::cout << "second solution" << std::endl;

    auto p0 = &bots["output_0"];
    auto p1 = &bots["output_1"];
    auto p2 = &bots["output_2"];

    std::cout << "output_0: " << p0->high << std::endl;
    std::cout << "output_1: " << p1->high << std::endl;
    std::cout << "output_2: " << p2->high << std::endl;

    std::cout << "puzzle part 2 solution: " << (p0->high * p1->high * p2->high) << std::endl;
}

int main()
{
    auto txt = load_file("./d10.txt");
    solve_puzzle_1(txt, 61, 17);
    return 0;
}
