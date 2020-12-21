# simple_dcf_model

Free cash flow is the amount of cash available from operations after paying for capital expenditures (typically investment in new PPE). After paying the necessary fees with income, free cash flows is the portion of income available for investing and financing new projects. The unlevered cash in period $i$ can be calculated by the following equation:
$$
    CF_i = EBIT_i \times (1 - T) + DepAmo_i - \Delta w_i - CapEx_i (1)
$$
, where $CF$ is unlevered cash flow, $T$ is tax rate, $DepAmo$ is depreciation and amortization, $\Delta w$ is the changes in working capital, and $ CapEx $ is capital expenditure. Note that unlevered cash flow means cash flow before paying debt. The present value of unlevered cash flow is enterprise value. The enterprise value can be calculated by:
$$
EV = MC + D - C (2)
$$
, where $EV$ is the enterprise value, $MC$ is the market capitalization, which equals to the current stock price multiplied by the number of outstanding stock shares, $D$ is total debt and $C$ is cash and cash equivalent. Rearrange the equation above, we can derive the fair equity value by predicting the enterprise value:
$$
MC = EV - D + C (3)
$$

From equations above, we can further derive the fair value per share:
$$
f = \frac{\sum PV_i(CF_i) - D + C}{n} (4)
$$
, where $PV_i(CF_i)$ is the present value of cash flow in period $i$, $f$ is fair value per share (equity per share), $n$ is number of outstanding shares.

We assume that in the first period, the earning is growing at rate $g_e$, changes in working capital decreases at rate $g_w$ and capital expenditure is growing at rate $g_c$. And in the second period, the free cash flow is growing at risk free rate $r_{f}$. With these growth rate, we can predict the future cash flow:
$$
    EBIT_{i+1} &= EBIT_{i} \times (1 + g_e)\\
    DepAmo_{i+1} &= DepAmo_{i} \times (1 + g_e)\\
    \Delta w_{i+1} &= \Delta w_{i} \times (1 + g_w)\\
    CapExp_{i+1} &= CapExp_{i} \times (1 + g_c) (5)
$$

The discounted rate is weighted average cost of capital, which is calculated by:
$$
    r_{WACC} = r_{f} + \beta \times r_{p} (6)
$$
, where $\beta$ is the levered beta of the firm, $r_{p}$ is equity risk premium.

The latest financial statement and equation (5) are used to predict the corresponding data in the next period. And then use the prediction to calculate the data in next period after that period. After that, equation (4) is used to calculate the fair value per share based on the predicted future cash flow.
