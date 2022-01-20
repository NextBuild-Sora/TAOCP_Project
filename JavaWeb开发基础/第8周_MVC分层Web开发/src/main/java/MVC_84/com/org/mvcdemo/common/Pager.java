package MVC_84.com.org.mvcdemo.common;

public class Pager {
	 
    /**
     * 当前页码
     */
    private int currentPage = 1;
    /**
     * 总记录数
     */
    private int totalResults = 0;
    /**
     * 每页记录数
     */
    private int pageSize = 10;
 
    /**
     * 实例化分页bean
     */
    public Pager() { }
 
    /**
     * @param currentPage 当前页码
     * @param totalResults 总记录数
     * @param pageSize 每页记录数
     */
    public Pager(int currentPage, int totalResults, int pageSize) {
        this.currentPage = currentPage;
        this.totalResults = totalResults;
        this.pageSize = pageSize;
    }
 
    /**
     * @return 当前页码
     */
    public int getCurrentPage() {
        return currentPage;
    }
 
    /**
     * @param currentPage 当前页码
     */
    public void setCurrentPage(int currentPage) {
        this.currentPage = currentPage;
    }
 
    /**
     * @return 总页数
     */
    public int getTotalPages() {
        return (int) Math.ceil(totalResults / (double) pageSize);
    }
 
    /**
     * @return 开始记录数
     */
    public int getStartResults() {
        return (currentPage - 1) * pageSize;
    }
 
    /**
     * @return 总记录数
     */
    public int getTotalResults() {
        return totalResults;
    }
 
    /**
     * @param totalResults 总记录数
     */
    public void setTotalResults(int totalResults) {
        this.totalResults = totalResults;
    }
 
    /**
     * @return 每页记录数
     */
    public int getPageSize() {
        return pageSize;
    }
 
    /**
     * @param pageSize 每页记录数
     */
    public void setPageSize(int pageSize) {
        this.pageSize = pageSize;
    }
 
    /**
     * @return 是否有上页
     */
    public boolean hasPrevPages() {
        return currentPage > 1;
    }
 
    /**
     * @return 是否有下页
     */
    public boolean hasNextPages() {
        return currentPage < getTotalPages();
    }
 
}
